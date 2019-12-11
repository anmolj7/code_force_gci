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
        tk.Label(self.app, text="").grid(row=0)
        tk.Label(self.app, text="Enter the user's handle:").grid(row=1)
        tk.Entry(self.app, textvariable=self.string_var).grid(row=1, column=1, padx=(15, 10))
        self.button = tk.Button(self.app, command=self.print_res, textvariable=self.button_text)
        self.button_text.set('Get Results!')
        self.button.grid(row=2)
        #######################
        '''Creating Labels'''
        #######################
        self.Labels = []
        self.StringVars = [tk.StringVar() for _ in range(len(self.Label_Names))]
        for i, label in enumerate(self.Label_Names):
            self.Labels.append(tk.Label(self.app, textvariable=self.StringVars[i]))
            tk.Label(self.app, text=self.Label_Names[i]+":").grid(row=3+i, column=0)
            self.Labels[i].grid(row=3+i, column=1) #Packing 'em
        #######################
        self.app.mainloop()

    def print_res(self):
        details = self.user_details(self.string_var.get())
        if not details:
            self.StringVars[0].set('Can\'t find details of the given handle.')
        else:
            for i in range(len(self.Label_Names)):
                self.StringVars[i].set(f'{details[i]}')

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
