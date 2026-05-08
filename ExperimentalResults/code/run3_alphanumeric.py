from RenderLeaksRunner import RenderLeaksRunner

runner = RenderLeaksRunner(
    scenario_type="alphanumeric",
    item_list=[ "6", "8"],  # Passcode Length
    erro_k =  0    # Near-Miss Leakage
)

runner.run()