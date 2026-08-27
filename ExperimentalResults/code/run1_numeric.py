from RenderLeaksRunner import RenderLeaksRunner

runner = RenderLeaksRunner(
    scenario_type="numeric",
    item_list=["4","6","8","4_main"],
)

runner.run()