from flask import Flask, render_template, request, Blueprint

CONSTANT_MARGIN = 50

blueprint = Blueprint('blueprint', __name__, url_prefix='/')


def get_tree_list(height=8, brick='*'):
    result = []
    for j in range(height + 1):
        margin = height - 1
        for i in range(0, j):
            bricks = brick * (1 + 2 * i)
            margin_str = ' ' * (margin + CONSTANT_MARGIN)
            result.append(margin_str + bricks)
            margin -= 1
    return result


@blueprint.route('/', methods=['GET'])
def get():
    return render_template('form.html')


@blueprint.route('/', methods=['POST'])
def post():
    kwargs = {
        'height': int(request.form['height']),
        'brick': request.form['brick']
    }
    tree_rows = get_tree_list(**kwargs)
    return render_template('tree.html', tree_rows=tree_rows)
