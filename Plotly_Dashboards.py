import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("my_data.csv")
st.line_chart(df)
                    marker_color=color))
    return fig

# Servidor web é iniciado
app.run_server(debug=True)
