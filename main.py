"""
Rastreamento de objetos em vídeo usando OpenCV.

Uso:
    python main.py              # usa 'race.mp4' como padrão
    python main.py meu_video.mp4
"""

import sys
import cv2


def main():
    # Seleciona o vídeo (argumento ou padrão)
    caminho_video = sys.argv[1] if len(sys.argv) > 1 else "race.mp4"

    video = cv2.VideoCapture(caminho_video)
    if not video.isOpened():
        print(f"Erro: não foi possível abrir o vídeo '{caminho_video}'")
        sys.exit(1)

    ok, frame = video.read()
    if not ok:
        print("Erro: não foi possível ler o primeiro frame do vídeo.")
        video.release()
        sys.exit(1)

    # Cria o rastreador KCF
    rastreador = cv2.TrackerKCF.create()

    # Seleciona a região de interesse (ROI)
    bbox = cv2.selectROI("Selecione o objeto", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Selecione o objeto")

    if bbox == (0, 0, 0, 0):
        print("Nenhuma ROI selecionada. Encerrando.")
        video.release()
        sys.exit(0)

    rastreador.init(frame, bbox)

    # Loop principal de rastreamento
    while True:
        ok, frame = video.read()
        if not ok:
            break

        ok, bbox = rastreador.update(frame)

        if ok:
            x, y, w, h = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2, 1)
        else:
            cv2.putText(
                frame, "Erro ao rastrear o objeto",
                (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2
            )

        cv2.imshow("Tracking", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC para sair
            break

    # Libera recursos
    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
