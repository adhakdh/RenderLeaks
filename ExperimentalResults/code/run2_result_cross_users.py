import json
import statistics


# ============================================================
input_type_list = ["4", "6", "8"]
# ============================================================


for tmp_type in input_type_list:
    print(f"------------ [ {tmp_type} ] ------------")
    result_json_path = f"../lib/savedata/result_numeric_{tmp_type}_0.json"

    n_results = 1

    sra_topk_values = (
        1,
        3,
        10,
        20,
        30,
        40,
        50,
        100,
    )


    def get_user_id(file_path):

        file_name = (
            str(file_path)
            .replace("\\", "/")
            .split("/")[-1]
        )

        stem = file_name.rsplit(".", 1)[0]

        parts = stem.split("_")

        if len(parts) < 1:
            return None

        if not parts[0].startswith("user"):
            return None

        try:
            return int(parts[0][4:])

        except ValueError:
            return None

    with open(
        result_json_path,
        "r",
        encoding="utf-8"
    ) as json_file:

        Result_dict = json.load(json_file)


    user_results = {}


    for item_name, item_list in Result_dict.items():

        for item in item_list:
            if (
                not isinstance(item, (list, tuple))
                or len(item) < 2
            ):
                continue

            file_path = item[0]
            accuracy_list = item[1]

            if (
                not isinstance(accuracy_list, (list, tuple))
                or len(accuracy_list) < 3
            ):
                continue


            user_id = get_user_id(
                file_path
            )

            if user_id is None:

                print(
                    f"[Skip] Cannot identify user: "
                    f"{file_path}"
                )

                continue

            kra_top1 = float(
                accuracy_list[0]
            )

            kra_top3 = float(
                accuracy_list[1]
            )

            sra_dict = accuracy_list[2]


            if not isinstance(sra_dict, dict):

                print(
                    f"[Skip] Invalid SRA data: "
                    f"{file_path}"
                )

                continue


            if user_id not in user_results:

                user_results[user_id] = {

                    "file_num": 0,

                    "KRA_T-1": [],
                    "KRA_T-3": [],
                }

                for topk in sra_topk_values:

                    user_results[
                        user_id
                    ][
                        f"SRA_T-{topk}"
                    ] = []


            user_results[
                user_id
            ][
                "file_num"
            ] += 1


            user_results[
                user_id
            ][
                "KRA_T-1"
            ].append(
                kra_top1
            )


            user_results[
                user_id
            ][
                "KRA_T-3"
            ].append(
                kra_top3
            )

            for topk in sra_topk_values:

                sra_key = f"top{topk}"

                if sra_key not in sra_dict:

                    raise KeyError(
                        f"{sra_key} not found:\n"
                        f"{file_path}\n"
                        f"{sra_dict}"
                    )

                user_results[
                    user_id
                ][
                    f"SRA_T-{topk}"
                ].append(
                    float(
                        sra_dict[sra_key]
                    )
                )

    metric_names = [

        "KRA_T-1",
        "KRA_T-3",

        "SRA_T-1",
        "SRA_T-3",
        "SRA_T-10",
        "SRA_T-20",
        "SRA_T-30",
        "SRA_T-40",
        "SRA_T-50",
        "SRA_T-100",
    ]


    per_user_results = {}


    for user_id in sorted(user_results):

        user_data = user_results[
            user_id
        ]

        per_user_results[
            user_id
        ] = {

            "File_num":
                user_data["file_num"]

        }


        for metric_name in metric_names:

            values = user_data[
                metric_name
            ]

            if len(values) == 0:

                per_user_results[
                    user_id
                ][metric_name] = 0.0

            else:

                per_user_results[
                    user_id
                ][metric_name] = (
                    statistics.mean(values)
                )


    for user_id in sorted(per_user_results):

        result = per_user_results[
            user_id
        ]


    mean_values = {}
    std_values = {}


    for metric_name in metric_names:

        values = [

            per_user_results[
                user_id
            ][metric_name]

            for user_id
            in sorted(per_user_results)

        ]


        mean_values[
            metric_name
        ] = statistics.mean(
            values
        )

        if len(values) > 1:

            std_values[
                metric_name
            ] = statistics.stdev(
                values
            )

        else:

            std_values[
                metric_name
            ] = 0.0

    total_file_num = sum(
        result["File_num"]
        for result in per_user_results.values()
    )


    summary_header = [
        "File_num"
    ]

    for metric_name in metric_names:

        summary_header.append(
            f"{metric_name}_Mean"
        )

        summary_header.append(
            f"{metric_name}_Std"
        )


    summary_row = [
        str(total_file_num)
    ]

    for metric_name in metric_names:

        summary_row.append(
            f"{mean_values[metric_name]:.3f}"
        )

        summary_row.append(
            f"{std_values[metric_name]:.3f}"
        )


    print(
        f"Total files: "
        f"{total_file_num}"
    )

    print()

    print(
        ",".join(summary_header)
    )

    print(
        ",".join(summary_row)
    )
    print()
