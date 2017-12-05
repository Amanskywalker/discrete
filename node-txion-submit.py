from flask import Flask
from flask import request
node = Flask(__name__)

# Node list
this_nodes_transactions = []

@node.route('/txion', methods=['POST'])
def transaction():
  if request.method == 'POST':
    # Activate only on POST request
    new_txion = request.get_json()
    # Add the transaction in the list
    this_nodes_transactions.append(new_txion)
    # Because the transaction was successfully
    # submitted, we log it to our console
    print "New transaction"
    print "FROM: {}".format(new_txion['from'])
    print "TO: {}".format(new_txion['to'])
    print "AMOUNT: {}\n".format(new_txion['amount'])
    # Then we let the client know it worked out
    return "Transaction submission successful\n"

node.run()
