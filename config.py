######################
## STAGE MANAGEMENT ##
######################

from importlib import import_module

stage_tree = []

run_game = True

def switch_stage(new_stage: str, save_previous_stage: bool = False):
    global stage_tree

    if not save_previous_stage:
        stage_tree.pop(-1)

    mod = import_module(f'stages.{new_stage}')
    stage_tree.append(getattr(mod, f'init_{new_stage}')())

    #print([type(stage) for stage in stage_tree])

def restore_last_stage():
    global stage_tree
    
    stage_tree.pop(-1)

    #print([type(stage) for stage in stage_tree])


def reset_tree():
    global stage_tree

    from stages.mainmenu import init_mainmenu
    stage_tree = [init_mainmenu()]

    #print([type(stage) for stage in stage_tree])