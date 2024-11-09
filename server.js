const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors'); // เพิ่มการเรียกใช้งาน cors

const app = express();
const { spawn } = require('child_process');
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: '*', // หรือระบุโดเมนที่ต้องการอนุญาต
    methods: ['GET', 'POST']
  }
});

// ใช้ cors กับ express
app.use(cors());



app.get('/', (req, res) => {
  res.send('Hello! Think keng!');
});

let pythonProcess;
let pythonProcessCount = 0;

io.on('connection', (socket) => {
  console.log('WebSocket client connected');

  // pythonProcess = spawn('python', ['model.py']);
  // pythonProcessCount++;
  // console.log('pythonProcess executed', pythonProcessCount);

  if (!pythonProcess) {
    pythonProcess = spawn('python', ['model.py']);
    pythonProcessCount++; 
    // pythonProcess = spawn('python', ['test2.py']);
    console.log('pythonProcess executed', pythonProcessCount);
  }

  // เรียกใช้ yolo.py เมื่อมีการเชื่อมต่อ
  // if (!pythonProcess) {
  //   pythonProcess = spawn('python', ['model.py']);
  //   console.log('pythonProcess executed');

  //   socket.on('processed_frame', (frame) => {
  //     io.emit('to_python_frame', frame);
  //     // console.log("frame:", frame);
  //   })
    
  
  //   socket.on('from_python_frame', (frame) => {
  //     // console.log("frame:", frame);
  //     io.emit('result_frame', frame);
  //   });
  
  //   socket.on('disconnect', () => {
  //     console.log('WebSocket client disconnected');
  //     if (pythonProcess) {
  //       pythonProcess.kill(); // หยุดกระบวนการ Python เมื่อ client หลุด
  //     }
  //   });
  // }
  // pythonProcess = spawn('python', ['model.py']);

  pythonProcess.stdout.on('data', (data) => {
    console.log(`Output from Python script: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Error from Python script: ${data}`);
  });

  pythonProcess.on('close', (code) => {
    console.log(`Python script exited with code ${code}`);
  });

  socket.on('processed_frame', (frame) => {
    // console.log("received frame from client:", frame);
    io.emit('to_python_frame', frame);
    // console.log("frame:", frame);
  })
  

  socket.on('from_python_frame', (frame) => {
    // console.log("received frame from python:", frame);
    // console.log("frame:", frame);
    io.emit('result_frame', frame);
  });

  socket.on('disconnect', () => {
    console.log('WebSocket client disconnected');
    if (pythonProcess) {
      pythonProcess.kill(); // หยุดกระบวนการ Python เมื่อ client หลุด
      pythonProcess = null;
    }
  });
});

const PORT = process.env.PORT || 5501;
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
