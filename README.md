# Charles Shaju

**Embedded Systems & Robotics Engineer** · Kochi, Kerala, India

Autonomous surface vehicles, underwater ROVs and ROS 2 mobile robots. MCA student at Rajagiri College of Social Science.

[Portfolio](https://charles-shaju.lovable.app) · [LinkedIn](https://linkedin.com/in/charles-shaju) · [Email](mailto:charlesshaju00@gmail.com)

---

## About

I work on the electronics, control tuning and software that make marine and mobile robots run reliably in the field. At i4 Marine Technologies I have worked on a catamaran ASV used for bathymetry surveys and an underwater ROV used for dam inspection, across four dam sites. Outside work, I am building a ROS 2 mobile robot for sensor fusion and obstacle avoidance, and I am learning modern C++.

I am looking for robotics engineering roles and internships.

---

## Experience

### Embedded Systems Engineer, i4 Marine Technologies
*Currently part-time alongside my MCA*

- **Catamaran ASV** (80 kg payload) for dam bathymetry, water-quality testing and fish feeding. Worked on ArduPilot/Pixhawk configuration, the modem and UDP communication link, the sensor data UI, electronics debugging, maintenance and field testing.
- **Control tuning:** tuned PID gains (steering, speed, acceleration) for waypoint tracking and line following, using Mission Planner gyro graphs and logs. This fixed the vessel zigzagging; after tuning it followed the planned path with under 1 m drift.
- **Field work:** bathymetry surveys and dam wall inspections at four dams, run as a service.
- **Underwater ROV:** electronics, software configuration, wiring, calibration and testing. Also worked on a commercial BlueROV.
- **IoT modules:** GPS modules for outboard motors, a precision barometer, and speed-control modules for electric canoes.
- **In progress:** a ROS 2 mobile robot prototype with obstacle avoidance, intended for the catamaran.

### EdTech & Robotics Solutions Engineer (Intern), Jobin & Jismi
*Apr 2026 – May 2026*

- Built a web platform with Google Blockly and JavaScript that connects over Bluetooth to an ESP32-based educational robot, so students can drive it and program it with blocks.
- Tested and debugged the educational robot.

### Robotics Intern, Shristi Robotics

- Built a 6-thruster underwater ROV (Pixhawk, ArduSub) under a professor's guidance: wiring, calibration and testing. It was used to inspect a dam.
- Operated 3D printers; basic CAD in Onshape.
- Taught a 2-week summer class for school students and one-day workshops for college students on mobile robotics and Arduino.

---

## Projects

| Project | Description |
|---|---|
| [**ROS 2 sensor-fusion rover**](https://github.com/charles-shaju/ROS) | Raspberry Pi running ROS 2 Humble, ESP32 for motors and encoders, BNO085 IMU, and a TFmini lidar swept by a stepper motor. Kalman-filter fusion of IMU and wheel encoders; odometry and live scan in RViz. Work in progress. |
| **Nut and bolt detection** | RF-DETR Small fine-tuned on 1,647 annotated images, with ByteTrack tracking and per-class line counting, built with Roboflow. |
| [**CNC pen plotter**](https://github.com/charles-shaju/CNC-Plotter) | A3 two-axis Cartesian XY plotter with a pen-lift servo. GRBL running on ESP32 via FluidNC, with hand-soldered electronics and 3D-printed parts. |
| [**OBM-IoT**](https://github.com/charles-shaju/OBM-IoT) | Embedded firmware for IoT modules on outboard motors, developed at i4 Marine. |
| [**Smart Altimeter**](https://github.com/charles-shaju/Smart_Altimeter) | Barometric altimeter on ESP32/Arduino with mean-sea-level altitude calculation. |
| [**Intelligent Voice Assistant**](https://github.com/charles-shaju/Intelligent-Voice-Assistant) | Python voice assistant using a TensorFlow intent classifier, SpeechRecognition and pyttsx3. |

---

## Skills

| Area | Tools |
|---|---|
| Robotics | ROS 2 Humble, ArduPilot / ArduSub, Pixhawk, Mission Planner, QGroundControl, PID tuning, Kalman filtering |
| Embedded | ESP32, STM32, Raspberry Pi, Arduino, PlatformIO, I2C, SPI, UART, UDP |
| Languages | Python, C/C++ (Arduino framework), JavaScript |
| Vision & ML | Roboflow, RF-DETR, ByteTrack, TensorFlow, Intel RealSense D455 |
| Tooling | Git, GitHub, Docker, Linux |

---

## Patent

Co-inventor on Indian patent application No. 202421040473, *An Underwater Remotely Operated Vehicle for Structural Health Monitoring (UROV-SHM)*. Filed 24 May 2024, published 12 Jul 2024, currently under examination.

## Certifications

- MathWorks Computer Vision Engineer (2026)
-  ASAP Kerala: AI-Machine Learning Developer (2024)
- ISRO: Geodata Processing using Python & ML (2025)

---

## Currently

- Building the ROS 2 rover toward SLAM mapping and camera + lidar obstacle avoidance
- Learning C++ for robotics
