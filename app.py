import streamlit as st
import pandas as pd
from sqlalchemy import text
from connection import engine

st.set_page_config(page_title="📚 Book Store Data App", layout="wide")

st.title("📚 Book Store Analytics")

# ---------- Sidebar Filters ----------
st.sidebar.header("Filter Books")

author = st.sidebar.text_input("Author Name")
genre = st.sidebar.selectbox("Genre", ["", "Biography", "Mystery", "Science Fiction", "Fantasy","Romance","Non-Fiction","Fantasy"])
year = st.sidebar.number_input("Published Year",value=2000)

# ---------- Build Dynamic Query ----------
query = """
SELECT * FROM new.default.book
WHERE published_year = :year
"""

params = {
    "year": year
}

if author:
    query += " AND author = :author"
    params["author"] = author

if genre:
    query += " AND genre = :genre"
    params["genre"] = genre

query += " ORDER BY published_year DESC"

# ---------- Fetch Data ----------
with engine.connect() as conn:
    result = conn.execute(text(query), params)
    df = pd.DataFrame(result.fetchall(), columns=result.keys())

# ---------- Show Data ----------
st.subheader("Filtered Books")
st.dataframe(df)

# ---------- KPIs ----------
st.subheader("📊 Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Books", len(df))
col2.metric("Total Stock", int(df["Stock"].sum()) if not df.empty else 0)
col3.metric("Avg Price", round(df["Price"].mean(),2) if not df.empty else 0)
