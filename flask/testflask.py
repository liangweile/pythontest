from flask import Flask
app = Flask(__name__)
@app.route('/')
def liangweile():
    return "liangweile"
@app.route('/hello')
def hello():
    return "hello, world"
@app.route('/user/<username>')
def user(username):
    return username
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
@app.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':


if __name__ == "__main__":
    app.run(debug=True)
