if (request.method == 'POST'):
        genre_name = request.form["genre_name"]
        genresData = searchGenre(sqlserver, genre_name)
        return render_template("genres.html", genresData=genresData)
