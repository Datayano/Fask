from flask import Blueprint
from flask import render_template
import pandas as pd

bp = Blueprint('main', __name__)

def full_path(suffixe):
    prefix = "https://image.tmdb.org/t/p/w300"
    full_path = prefix + suffixe   
    return full_path

@bp.route('/')
def index():
    
    df_tmdb = pd.read_csv('https://raw.githubusercontent.com/Phil-BENISSAN/tmdb/main/tmdb_small.csv')
    df_reduit = df_tmdb[["original_title", "overview", "vote_average", "poster_path"]]
    df_reduit["poster_path"] = df_reduit["poster_path"].apply(full_path)
    df_reduit.sort_values(by= "vote_average", ascending=False, inplace=True)
    df_reduit = df_reduit.head()
    datas = [line[1] for line in df_reduit.iterrows()]

    return render_template('index.html', title='Home Page', datas=datas)


@bp.route('/about')
def about():
    return render_template('about.html', title='About')