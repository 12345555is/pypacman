import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from runner import GameRun

if __name__=='__main__':
    gr = GameRun()
    gr.main()
