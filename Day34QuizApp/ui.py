from tkinter import*
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial",20,"italic")

class QuizInterface:
  
  def __init__(self,quiz_brain: QuizBrain) -> None:
    self.quiz = quiz_brain
    
    self.window = Tk()
    self.window.title('Quizler')
    self.window.config(padx=20,pady=20,bg=THEME_COLOR)
    
    self.score = Label(text='Score: 0',bg=THEME_COLOR,fg='white')
    self.score.grid(column=1,row=0)
    
    self.canvas = Canvas()
    self.canvas.config(height=250,width=300)
    self.question_text = self.canvas.create_text(
      150,
      125,
      width=280,
      text='test',
      font=FONT)
    self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
    
    self.true_img = PhotoImage(file='Day34QuizApp/images/true.png')
    self.true_btn = Button(image=self.true_img,bg=THEME_COLOR,borderwidth=0,command=self.answer_true)
    self.true_btn.grid(column=0,row=2,pady=20)

    self.false_img = PhotoImage(file='Day34QuizApp/images/false.png')
    self.false_btn = Button(image=self.false_img,bg=THEME_COLOR,borderwidth=0,command=self.answer_false)
    self.false_btn.grid(column=1,row=2,pady=20)
    
    self.show_next_question()
    
    self.window.mainloop()
    
  def show_next_question(self):
    self.canvas.config(bg='white')
    if self.quiz.still_has_questions():
      self.score.config(text=f'Score: {self.quiz.score}')
      quiz_text = self.quiz.next_question()
      self.canvas.itemconfig(self.question_text,text=quiz_text)
    else:
      self.canvas.itemconfig(self.question_text,text=f'Quiz Completed!\n Score: {self.quiz.score}/10')
      self.true_btn.config(state=DISABLED)
      self.false_btn.config(state=DISABLED)
   
  def answer_true(self):
    self.give_feedback(self.quiz.check_answer('True'))
    
  def answer_false(self):
    self.give_feedback(self.quiz.check_answer('False'))
    
  def give_feedback(self, is_right):
    if is_right ==True:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    self.window.after(1000,self.show_next_question)
    

    
