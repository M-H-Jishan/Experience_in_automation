from transitions import Machine

class DialogueManager:
    states = ['greeting', 'inquiring', 'shopping', 'checkout']

    def __init__(self):
        self.machine = Machine(model=self, states=DialogueManager.states, initial='greeting')
        
        self.machine.add_transition('greet', 'greeting', 'inquiring')
        self.machine.add_transition('inquire', 'inquiring', 'inquiring')
        self.machine.add_transition('shop', 'inquiring', 'shopping')
        self.machine.add_transition('shop', 'shopping', 'shopping')
        self.machine.add_transition('finish', 'shopping', 'checkout')
        self.machine.add_transition('reset', '*', 'greeting')

    def get_state(self):
        return self.state