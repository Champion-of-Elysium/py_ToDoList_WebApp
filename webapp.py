import streamlit as stlit
from functions import get_todos, write_todos

todos = get_todos()

stlit.set_page_config(layout="wide")


def add_todo():
    todo = stlit.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)


stlit.title("My Todo Web App")
stlit.subheader("This is my todo app.")
stlit.write("This app is to increase your <b>productivity</b>.",
            unsafe_allow_html=True)

for index, new_todo in enumerate(todos):
    checkbox = stlit.checkbox(new_todo, key=new_todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del stlit.session_state[new_todo]
        stlit._rerun()

stlit.text_input(label="", placeholder="Add new todo...",
                 on_change=add_todo, key="new_todo")
