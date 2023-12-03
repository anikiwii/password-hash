Hashowanie haseł: użyjemy algorytmu SHA-256 do hashowania hasła.

kolejne kroki:
Importujemy moduł hashlib, który umożliwia korzystanie z różnych algorytmów haszujących, takich jak SHA-256.Tworzymy funkcję generate_hash(password), która przyjmuje hasło jako argument, tworzy obiekt haszujący przy użyciu SHA-256, aktualizuje go bajtami hasła, a następnie zwraca zhashowane hasło w formie szesnastkowej reprezentacji.Tworzymy funkcję verify_password(entered_password, stored_hash), która przyjmuje wprowadzone hasło i zhashowane hasło przechowywane w bazie danych. Funkcja haszuje wprowadzone hasło i porównuje z hasłem przechowywanym. Jeśli są zgodne, hasło jest poprawne.Na końcu przykładu używamy funkcji do wygenerowania zhashowanego hasła (stored_password_hash) i symulujemy próbę logowania, prosząc użytkownika o wprowadzenie hasła. Wprowadzone hasło jest następnie weryfikowane przez funkcję verify_password.