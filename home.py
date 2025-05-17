from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Temporary storage for registered users
users = []

@app.route('/')
def landing_page():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')  # You can split your HTML into templates

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']
        user_type = request.form['user_type']
        
        # Dummy auth logic
        for user in users:
            if user['email'] == email and user['phone'] == phone and user['user_type'] == user_type:
                return f"Welcome back, {user['name']} ({user_type})!"
        return "User not found or incorrect details!"
    
    return render_template('signin.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_type = request.form['user_type']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        services = request.form['services']
        
        user = {
            'user_type': user_type,
            'name': name,
            'email': email,
            'phone': phone,
            'services': services
        }
        users.append(user)
        return f"Registered successfully as {user_type}! Welcome, {name}."

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
