from flask import Flask,render_template

FAI=Flask( __name__ )

@FAI.route('/wish/<name>')
def wish(name):

    return f'Hi {name} how r u'
@FAI.route('/first')
def first():
    return render_template('first.html',name='Dinesh')

@FAI.route('/second')
def second():
    return render_template('second.html',name='Dinesh')

if __name__=='__main__':
    FAI.run(debug=True)

