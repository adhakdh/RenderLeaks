from RenderLeaksRunner import RenderLeaksRunner

runner = RenderLeaksRunner(
    scenario_type="31key",
    item_list=["31key"],
       erro_k =  0,    
       if_keyboard_anchor=1   # Keyboard Position Availability
)

runner.run()