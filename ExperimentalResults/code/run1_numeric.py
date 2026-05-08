from RenderLeaksRunner import RenderLeaksRunner

runner = RenderLeaksRunner(
    scenario_type="numeric",
    item_list=["4","6","8"],  # Passcode Length
    erro_k = 0,  # Near-Miss Leakage
    if_keyboard_anchor=0,  # Keyboard Position Availability
)

runner.run()