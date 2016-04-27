from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github','jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    grades = hackbright.get_grades_by_github(github)
    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            grades=grades
)
    return html

@app.route("/student-search")
def get_student_form():
    """Student search form"""

    return render_template("student_search.html")


@app.route("/make_student")
def make_student():
    """Add a student"""

    return render_template("make-student.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """ Add a student to DB """

    #print request.form
    first = request.form['firstname']
    last = request.form['lastname']
    github = request.form['github']

    #add new student to Students table in Hackbright database
    #by calling the add student function
    hackbright.make_new_student(first, last, github)
    #display the results to the user with new student info
    return render_template('student-add.html', first=first, last=last, github=github) 


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
