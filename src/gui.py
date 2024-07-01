import tkinter as tk
from tkinter import messagebox
import backend

class ChatSessionManager:
    def __init__(self, root):
        self.root = root
        self.root.title("GPT Session Continuity Extender")

        self.session_label = tk.Label(root, text="Enter new session data:")
        self.session_label.pack()

        self.session_entry = tk.Text(root, height=10)
        self.session_entry.pack()

        self.save_button = tk.Button(root, text="Save Session", command=self.save_session)
        self.save_button.pack()

        self.load_button = tk.Button(root, text="Load Sessions", command=self.load_sessions)
        self.load_button.pack()

        self.sessions_display = tk.Text(root, height=10)
        self.sessions_display.pack()

        self.session_count_label = tk.Label(root, text="Sessions loaded: 0")
        self.session_count_label.pack()

    def save_session(self):
        session_data = self.session_entry.get("1.0", tk.END).strip()
        if session_data:
            backend.save_session(session_data)
            self.session_entry.delete("1.0", tk.END)
            messagebox.showinfo("Success", "Session saved successfully!")
        else:
            messagebox.showwarning("Warning", "Session data cannot be empty!")

    def load_sessions(self):
        sessions = backend.load_sessions()
        self.sessions_display.delete("1.0", tk.END)
        for session in sessions:
            self.sessions_display.insert(tk.END, session + "\n\n")
        self.session_count_label.config(text=f"Sessions loaded: {len(sessions)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatSessionManager(root)
    root.mainloop()
