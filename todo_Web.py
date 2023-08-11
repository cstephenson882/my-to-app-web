import streamlit as st
import functions

todos = functions.readToDO()
def add_todo():
    todo = st.session_state['new_todo']
    if not todo == "":
        todos.append(todo+'\n')
        functions.writeToDo(todos)

st.title('My Todo App')
st.subheader("This is my todo app!")
st.write('This app is to increase your productivity')

for index,todo in enumerate(todos):

    checkbox = st.checkbox(todo, key = todo)
    #print('checkbox: ',checkbox)
    if checkbox:
        todos.pop(index)
        functions.writeToDo(todos)

        # reloading session so that the removed to is displayed in the GUI
        del st.session_state[todo]
        st._rerun()

st.text_input("", placeholder='enter a todo...',key='new_todo', on_change= add_todo)
