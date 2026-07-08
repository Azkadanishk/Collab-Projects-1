import cv2

def scan_qr():

    detector = cv2.QRCodeDetector()

    kamera = cv2.VideoCapture(0)

    if not kamera.isOpened():
        print("Kamera tidak bisa diakses")
        return None

    print("Scan QR...")

    while True:

        ret, frame = kamera.read()

        if not ret:
            break

        data, bbox, _ = detector.detectAndDecode(frame)

        if data:
            print("QR terbaca:", data)

            kamera.release()
            cv2.destroyAllWindows()

            return data
        cv2.imshow("QR Scanner", frame)

        if cv2.waitKey(1) == 27:
            break
    
    kamera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr()