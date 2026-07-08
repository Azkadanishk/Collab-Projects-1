import cv2
import time

def scan_once():
    detector = cv2.QRCodeDetector()

    kamera = cv2.VideoCapture(0)

    if not kamera.isOpened():
        print("Kamera tidak ditemukan!")
        return None
    print("Scan QR Siswa...")

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
        
        cv2.imshow(
            "Perpustakaan QR Scanner",
            frame
        )

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):

            kamera.release()
            cv2.destroyAllWindows()

            return None
        
def scan_qr_realtime(callback):

    detector = cv2.QRCodeDetector()

    kamera = cv2.VideoCapture(0)

    if not kamera.isOpened():
        print("Kamera tidak bisa diakses")
        return 

    print("Scanner aktif...")

    waktu_scan = 0
    cooldown = 3

    while True:

        ret, frame = kamera.read()

        if not ret:
            break

        data, bbox, _ = detector.detectAndDecode(frame)

        if data:
            sekarang = time.time()
            if sekarang - waktu_scan > cooldown:
                waktu_scan = sekarang
                print("QR:", data)
                callback(data)

        cv2.imshow(
            "Scanner Absensi",
            frame
        )

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            print("Scanner berhenti...")
            break
    
    kamera.release()
    cv2.destroyAllWindows()
