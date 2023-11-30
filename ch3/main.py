import time, sys

indent = 0
indent_increase = True


try:
    while True:
        print(" "*indent+"********")
        time.sleep(0.1)
        
        if indent_increase == True:
            indent+=1
            if indent >= 10:
                indent_increase = False

        else:
            indent -= 1
            if indent <= 0:
                indent_increase = True


            
except KeyboardInterrupt:
    sys.exit()
            
