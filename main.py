'''
To Fetch: Handle, Current Rating, Rank, Max Rating , Max Rank 
'''
import requests
import tkinter as tk
import time

class App:
    Label_Names = [
        'Current Rating',
        'Rank',
        'Maximum Rating',
        'Maximum Rank'
    ]
    def __init__(self):
        self.app = tk.Tk()  
        self.app.title('CodeForceGCI')
        self.string_var = tk.StringVar()
        self.button_text = tk.StringVar()
        #######################
        '''Creating Widgets'''
        #######################
        tk.Label(self.app, text="Enter the user's handle").pack()
        tk.Entry(self.app, textvariable=self.string_var).pack()
        self.button = tk.Button(self.app, command=self.print_res, textvariable=self.button_text)
        self.button_text.set('Get Results!')
        self.button.pack()
        #######################
        '''Creating Labels'''
        #######################
        self.Labels = []
        self.StringVars = [tk.StringVar() for _ in range(len(self.Label_Names))]
        for i, label in enumerate(self.Label_Names):
            self.Labels.append(tk.Label(self.app, textvariable=self.StringVars[i]))
            self.Labels[i].pack() #Packing 'em
        #######################
        self.app.mainloop()

    def print_res(self):
        details = self.user_details(self.string_var.get())
        if not details:
            self.StringVars[0].set('Can\'t find details of the given handle.')
        else:
            for i in range(len(self.Label_Names)):
                self.StringVars[i].set(f'{self.Label_Names[i]}: {details[i]}')

    def user_details(self, handle):
        try:
            self.button_text.set('Getting results.')
            self.button['state'] = 'disabled'
            handle = str(handle)
            url = f'https://codeforces.com/api/user.rating?handle={handle}'
            user_data = requests.get(url).json()
            RANKS, RATINGS = [], []
            for data in user_data['result']:
                RANKS.append(data['rank'])
                RATINGS.append(data['newRating'])
            self.button['state'] = 'normal'
            self.button_text.set('Get Results!')
            return RATINGS[-1], RANKS[-1], max(RATINGS), min(RANKS)
        except:
            self.button['state'] = 'normal'
            self.button_text.set('Get Results!')
            return None


def main():
    App()
    

if __name__ == "__main__":
    main()
