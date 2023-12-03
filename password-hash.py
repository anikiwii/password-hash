import hashlib

def generate_hash(password):
    # Tworzymy obiekt haszujący przy użyciu algorytmu SHA-256
    sha256 = hashlib.sha256()

    # Konwertujemy hasło na bajty (UTF-8) i przekazujemy do obiektu haszującego
    sha256.update(password.encode('utf-8'))

    # Pobieramy zhashowane hasło jako szesnastkową reprezentację
    hashed_password = sha256.hexdigest()

    return hashed_password

def verify_password(entered_password, stored_hash):
    # Haszujemy wprowadzone hasło
    entered_password_hashed = generate_hash(entered_password)

    # Porównujemy hasła
    if entered_password_hashed == stored_hash:
        print("Hasło poprawne.")
    else:
        print("Błąd: Nieprawidłowe hasło.")