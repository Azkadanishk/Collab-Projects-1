import cv2

def scan_qr(callback):

    detector = cv2.QRCodeDetector()

    kamera = cv2.VideoCapture(0)

    if not kamera.isOpened():
        print("Kamera tidak bisa diakses")
        return None

    print("Scanner aktif...")

    terakhir = None

    while True:

        ret, frame = kamera.read()

        if not ret:
            break

        data, bbox, _ = detector.detectAndDecode(frame)

        if data:
            if data != terakhir:
                terakhir = data
                print("QR:", data)
                callback(data)

        cv2.imshow(
            "Scanner Absensi",
            frame
        )

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    
    kamera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr()