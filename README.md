# Cold Rolling Mill Motor Speed Control using PID on Arduino Opta PLC

## 📌 Overview
This project demonstrates a **closed-loop speed control system** for DC motors in the **Cold Rolling Mill of Rourkela Steel Plant (SAIL)**.  
We implemented a **PID controller on Arduino Opta PLC**, integrated with **encoders** and **current sensors** for feedback, while firing a **thyristor stack** to regulate motor speed and torque.  
The system incorporates **Kalman filtering** and **IIR digital filters** for noise reduction, ensuring stable and precise control under industrial conditions.  

---

## ⚙️ Features
- **PID Control System**: Closed-loop control implemented on Arduino Opta PLC.  
- **Sensor Integration**: Encoder feedback (±1 RPM resolution) and Hall-effect current sensors (up to 50 A).  
- **Filtering Techniques**: Kalman filter and IIR filter for smoothing noisy sensor data.  
- **Power Electronics**: Thyristor stack firing module synchronized with AC mains for variable DC drive.  
- **Performance Gains**:
  - Reduced speed fluctuations by **~18%** compared to open-loop.  
  - Measurement noise reduced by **>40%**.  
  - Overshoot and settling time improved by **~22%**.  

---

## 🛠️ System Architecture
1. **Input Acquisition**
   - Encoder → Motor speed feedback  
   - Current sensor → Load current measurement  

2. **Signal Conditioning**
   - Kalman Filter (state estimation)  
   - IIR Filter (low-pass smoothing)  

3. **Controller**
   - PID algorithm tuned for industrial dynamics  
   - Output: control signal for thyristor firing  

4. **Actuation**
   - Thyristor stack firing circuit → DC motor voltage control  

---

## 📊 Block Diagram
<img width="1024" height="1024" alt="Gemini_Generated_Image_5qzhjo5qzhjo5qzh" src="https://github.com/user-attachments/assets/042a0362-4a9b-40b7-b9a9-caf187eee0b4" />

