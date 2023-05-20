import cv2
import mediapipe as mp

# somewhere in the main code, defining Mediapipe pose model
# and then pass to pose argument
pose = mp.solutions.pose.Pose(
            min_detection_confidence=0.5, min_tracking_confidence=0.5)

def human_mediapipe_detection(image_path, pose):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    image_height, image_width, _ = image.shape
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if results.pose_landmarks:
        landmark = results.pose_landmarks.landmark
        left_eye = landmark[2]
        right_eye = landmark[5]
        head = [(left_eye.x + right_eye.x) / 2 * image_width,
                (left_eye.y + right_eye.y) / 2 * image_height]

        right_hand = [landmark[16].x * image_width,
                      landmark[16].y * image_height]
        left_hand = [landmark[15].x * image_width,
                     landmark[15].y * image_height]
        right_foot = [landmark[28].x * image_width,
                      landmark[28].y * image_height]
        left_foot = [landmark[27].x * image_width,
                     landmark[27].y * image_height]

        y_trunk_lmid = (landmark[11].y + landmark[23].y) / 2
        y_trunk_llower = (y_trunk_lmid + landmark[23].y) / 2
        y_trunk_rmid = (landmark[12].y + landmark[24].y) / 2
        y_trunk_rlower = (y_trunk_rmid + landmark[24].y) / 2

        y_trunk = (y_trunk_llower + y_trunk_rlower) / 2 * image_height
        trunk = [(landmark[23].x + landmark[24].x) / 2 * image_width, y_trunk]

        keypoints = [head, trunk, right_hand, left_hand, right_foot, left_foot]
        return keypoints