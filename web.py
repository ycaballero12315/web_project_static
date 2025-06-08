import streamlit as st
from pakage_func.functions import write_elems, read_file, todos

st.set_page_config(page_title="My ToDo App", page_icon="📝")
todos = read_file()

def add_todo():
    todo = st.session_state('new_todo')
    todos.append(todo)
    write_elems(todos)

st.title('My Todo App')
st.subheader('This is my todo app.')
st.write('This app is to increase your productivity.')

for idx, t in enumerate(todos):
   chbox =  st.checkbox(t, key=f'todo_{idx}')
   if chbox:
       todos.pop(idx)
       write_elems(todos)
       del st.session_state[f'todo_{idx}']
    #    st.experimental_rerun()

input_text = st.text_input(label='', placeholder="Enter a ToDo...", key='new_todo', on_change=add_todo)

if st.button('Add ToDo'):
    if input_text:
        todos.append(input_text)
        write_elems(todos)
        st.success(f'Saved {input_text}')
    else:
        st.warning('Insert one ToDo before add to list') 

if st.button('Clear'):
    pass

