#import sys
#type(sys.path)
#sys.path.append('site-packages/bitcoin')
#<class 'list'>


#from os.path import dirname, abspath, join
#import sys

# Find code directory relative to our directory
#THIS_DIR = dirname(__file__)
#CODE_DIR = abspath(join(THIS_DIR, '..', 'bitcoin'))
#sys.path.append(CODE_DIR)

#for path in sys.path:
   # print(path)

import bitcoin 
import bitcoin.rpc
from bitcoin.wallet import CBitcoinSecret
from bitcoin.base58 import Base58ChecksumError
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.signmessage import BitcoinMessage, VerifyMessage, SignMessage
import hashlib
from bitcoin.core import Hash160
from bitcoin.core.script import CScript, OP_DUP, OP_HASH160, OP_EQUALVERIFY, OP_CHECKSIG, SignatureHash, SIGHASH_ALL
from bitcoin.wallet import CBitcoinSecret
from bitcoin.core import *
from bitcoin.wallet import *
import bitcoin, bitcoin.core, bitcoin.core.script, bitcoin.wallet
from bitcoin.core.scripteval import *


def SSLConnection ():
    #print(bitcoin.__file__)
    bitcoin.SelectParams('mainnet')

    proxy = bitcoin.rpc.Proxy()
    print(proxy.getnewaddress())

#SSLConnection()
#help('modules')

def B58Veri ():
    key = "5J3mBbAH58CpQ3Y5RNJpUKPE62SQ5tfcvU2JpbnkeyhfsYB1Jcn"
    key2 = "5J3mBbAH58CpQ3Y5RNJpUKPE62SQ5tfcvU2JpbnkeyhfsYB1Jcnada"
    try:
        secret = CBitcoinSecret(key)
        print(secret)
        secret2 = CBitcoinSecret(key2)
    except Base58ChecksumError:
        print("Invalid Base 58 Key")

#B58Veri()

def signMessage():

    key = "5J3mBbAH58CpQ3Y5RNJpUKPE62SQ5tfcvU2JpbnkeyhfsYB1Jcn"
    msg = "message to sign"
 
    secret = CBitcoinSecret(key)
    message = BitcoinMessage(msg)
    signature = SignMessage(secret, message)
 
    address = P2PKHBitcoinAddress.from_pubkey(secret.pub)
    message = BitcoinMessage(msg)
    verify = VerifyMessage(address, message, signature)
    print('Address: %s' % address)
    print('Message: %s' % msg)
    print('Signature: %s' % signature)
    print('Verified: %s' % verify)
    print("\n")
    print('Verify using bitcoin core this command:')
    print('\n`bitcoin-cli verifymessage %s \'%s\' \'%s\'`\n' % (address, signature.decode('ascii'), msg))

#signMessage()

def signHasGen():
    bitcoin.SelectParams('mainnet')
 
    h = hashlib.sha256(b'wallet secret key').digest()
    seckey = CBitcoinSecret.from_secret_bytes(h)
 
    # Creating Script Pub Key
    txin_scriptPubKey = CScript([OP_DUP, OP_HASH160, Hash160(seckey.pub), OP_EQUALVERIFY, OP_CHECKSIG])
    
    # lx corresponds to little endian hex
    txid = lx('010862f9588f760b4a007cc316baa38890d5e102dc8cee923aae396260e13cb1')
    vout = 0
 
    # Create the txin structure, which includes the outpoint
    txin = CMutableTxIn(COutPoint(txid, vout))
    #print(txin)
 
    # Creating Script Pub Key
    param = [OP_DUP, OP_HASH160, Hash160(seckey.pub), OP_EQUALVERIFY, OP_CHECKSIG]
    txin_scriptPubKey = CScript(param)
 
    # Create txout object
    txout = CMutableTxOut(0.001*COIN, CBitcoinAddress('1CaJbGDKkk2DzWNAgHs6sgMdMJZ9eXvCs7').to_scriptPubKey())
 
    # Create unsigned transaction
    tx = CMutableTransaction([txin], [txout])
 
    # Calculate the signature hash for that transaction
    sighash = SignatureHash(txin_scriptPubKey, tx, 0, SIGHASH_ALL)
    print(sighash)

#signHasGen()
 
def p2pkhTransSpend():

    bitcoin.SelectParams('mainnet')
    
    h = hashlib.sha256(b'wallet secret key').digest()
    seckey = CBitcoinSecret.from_secret_bytes(h)
    
    # lx corresponds to little endian hex
    txid = lx('010862f9588f760b4a007cc316baa38890d5e102dc8cee923aae396260e13cb1')
    vout = 0
    
    # Create the txin structure, which includes the outpoint
    txin = CMutableTxIn(COutPoint(txid, vout))
    print(txin)
    
    # Creating Script Pub Key
    param = [OP_DUP, OP_HASH160, Hash160(seckey.pub), OP_EQUALVERIFY, OP_CHECKSIG]
    txin_scriptPubKey = CScript(param)
    
    # Create txout object
    txout = CMutableTxOut(0.001*COIN, CBitcoinAddress('1CaJbGDKkk2DzWNAgHs6sgMdMJZ9eXvCs7').to_scriptPubKey())
    
    # Create unsigned transaction
    tx = CMutableTransaction([txin], [txout])
    
    sighash = SignatureHash(txin_scriptPubKey, tx, 0, SIGHASH_ALL)
    
    sig = seckey.sign(sighash) + bytes([SIGHASH_ALL])
    
    txin.scriptSig = CScript([sig, seckey.pub])
    
    VerifyScript(txin.scriptSig, txin_scriptPubKey, tx, 0, (SCRIPT_VERIFY_P2SH,))
    
    print(bitcoin.core.b2x(tx.serialize()))

p2pkhTransSpend()