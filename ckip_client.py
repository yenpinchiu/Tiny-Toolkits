import socket

def ckip(query):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 1501))
    query = "<?xml version=\"1.0\" ?><wordsegmentation version=\"0.1\" charsetcode=\"utf-8\"><option showcategory=\"1\" /><authentication username=\"_tester\" password=\"tester\" /><text>"+query+"</text></wordsegmentation>" 
    sock.send(query.encode(encoding="UTF-8"))
    result = sock.recv(1048576).decode("utf-8").replace("</sentence><sentence>","").split("<sentence>")[1].split("</sentence>")[0]
    sock.close()
    return result
