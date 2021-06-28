<template>
  <div class="home pa-6">
    <h1>Sistema de medição, visualização e registro de temperaturas de
ambientes sensíveis.</h1>
<div class="mt-3 d-flex align-content-center flex-wrap" >
<div class="hame">
<v-card
    class="d-flex align-content-center flex-wrap"
    max-width="344"
    outlined
    elevation="7"
    width = "266"
    height= "324"
  >
 <v-card-text>
          <div class="font-weight-bold text-center">
                  <h2 style="font-family: Roboto;
font-style: normal;
font-weight: 500;
font-size: 22px;
line-height: 28px;" >Temperatura Sensor 1</h2>
          </div>
  </v-card-text>

  <v-row
  align="center"
  justify="center"
>
    <v-sheet
      class="text-center lighten-2 rounded-circle d-inline-flex align-center justify-center ma-3"
      height="220"
      width="220"
      elevation="7"
    >
    <v-icon color="rgba(0, 0, 255, 0.70)" size = "35" >mdi-thermometer</v-icon>
      <h1 style="color:rgba(0, 0, 255, 0.70); 
      font-family:Roboto; 
      font-style: normal;
      font-weight: 300;
      font-size: 24px;
      line-height: 28px;" >{{dados_sensor1}}°C</h1>
    </v-sheet>
    
</v-row>

  </v-card>
    </div>

    <div class="ml-5 hame">
<v-card
    class="d-flex align-content-center flex-wrap"
    max-width="344"
    outlined
    elevation="7"
    width = "266"
    height= "324"
  >
 <v-card-text>
          <div class="font-weight-bold text-center">
                  <h2 style="font-family: Roboto;
font-style: normal;
font-weight: 500;
font-size: 22px;
line-height: 28px;" >Temperatura Sensor 2</h2>
          </div>
  </v-card-text>

  <v-row
  align="center"
  justify="center"
>
    <v-sheet
      class="text-center lighten-2 rounded-circle d-inline-flex align-center justify-center ma-3"
      height="220"
      width="220"
      elevation="7"
    >
    <v-icon color="rgba(0, 0, 255, 0.70)" size = "35" >mdi-thermometer</v-icon>
      <h1 style="color:rgba(0, 0, 255, 0.70); 
      font-family:Roboto; 
      font-style: normal;
      font-weight: 300;
      font-size: 24px;
      line-height: 28px;" >{{dados_sensor2}}°C</h1>
    </v-sheet>
    
</v-row>

  </v-card>


    </div>


  </div>
    <div class="pt-6">
      <v-card
    class="text-center d-flex flex-wrap"
    color="rgba(243, 240, 215, .7)"
    dark
    elevation="8"
    
    >
      <v-card-text>
      <div class="text-h4 font-weight-thin">
        <p
        style="color:rgba(71,	89,	126, .8);
        font-family: Roboto;
font-style: normal;
font-weight: 400;"
        >Temperatura na Ultima Hora</p>
                <p
        style="color:rgba(71,	89,	126, .8);
        font-family: Roboto;
font-style: normal;
font-weight: 400;"
        >Sensor 1</p>
      </div>
    </v-card-text>
    <v-card-text>

      <v-sheet 
      class="rounded-l  align-center"
      color="rgba(255, 255, 25, .12)"
      elevation="4"
      
      >
        <v-sparkline
        class=" align-center"
          :value="dado"

          
          width = "800"
          height = "200"
          auto-draw
          color="rgba(71,	89,	126, .8)"
          
          padding="22"
          stroke-linecap="round"
          smooth
        >
          <template v-slot:label="dado">
            {{ dado.value }}
          </template>
        </v-sparkline>
      </v-sheet>
    </v-card-text>

    
  </v-card>
    </div>
        
        <div class="pt-6">
      <v-card
    class="mx-auto text-center"
    color="rgba(243, 240, 215, .7)"
    dark
    elevation="8"
    
    >
      <v-card-text>
      <div class="text-h4 font-weight-thin">
        <p
        style="color:rgba(71,	89,	126, .8);
        font-family: Roboto;
font-style: normal;
font-weight: 400;"
        >Temperatura na Ultima Hora</p>
                <p
        style="color:rgba(71,	89,	126, .8);
        font-family: Roboto;
font-style: normal;
font-weight: 400;"
        >Sensor 2</p>
      </div>
    </v-card-text>
    <v-card-text>

      <v-sheet 
      class="rounded-l  align-center"
      color="rgba(255, 255, 25, .12)"
      elevation="4"
      
      >
        <v-sparkline
        class=" align-center"
          :value="fetch_sensor2"

          
          width = "800"
          height = "200"
          auto-draw
          color="rgba(71,	89,	126, .8)"
          
          padding="22"
          stroke-linecap="round"
          smooth
        >
          <template v-slot:label="fetch_sensor2">
            {{ fetch_sensor2.value }}
          </template>
        </v-sparkline>
      </v-sheet>
    </v-card-text>

    
  </v-card>
    </div>



  </div>


</template>






<script>
// @ is an alias to /src

import mqtt from 'mqtt'
export default {
  name: 'Home',
data() {
    return {
      connection: {
        host: '192.168.1.2',
        port: 1884,
        endpoint: '',
        clean: true, // 保留会话
        connectTimeout: 4000, // 超时时间
        reconnectPeriod: 4000, // 重连时间间隔
        // 认证信息
        clientId: 'mqttjs_3be2c321',
        username: 'emqx_test',
        password: 'emqx_test',
      },
      subscription: {
        topic: 'home/sensor1',
        qos: 0,
        topic: 'home/sensor2',
        qos: 1,
      },
      publish: {
        topic: 'topic/browser',
        qos: 0,
        payload: '{ "msg": "Hello, I am browser." }',
      },
      dados_sensor1: '',
      dados_sensor2: '',
      qosList: [
        { label: 0, value: 0 },
        { label: 1, value: 1 },
        { label: 2, value: 2 },
      ],
      client: {
        connected: false,
      },
      subscribeSuccess: false,
      dado: [
      ],
      fetch_sensor2:[]
    }
  },
  methods: {
    // 创建连接
    createConnection() {
      // 连接字符串, 通过协议指定使用的连接方式
      // ws 未加密 WebSocket 连接
      // wss 加密 WebSocket 连接
      // mqtt 未加密 TCP 连接
      // mqtts 加密 TCP 连接
      // wxs 微信小程序连接
      // alis 支付宝小程序连接
      const { host, port, endpoint, ...options } = this.connection
      const connectUrl = `ws://${host}:${port}${endpoint}`
      try {
        this.client = mqtt.connect(connectUrl, options)
      } catch (error) {
        console.log('mqtt.connect error', error)
      }
      this.client.on('error', error => {
        console.log('Connection failed', error)
      })
      this.client.on('message', (topic, message) => {
        if(topic == 'home/sensor1'){
          this.dados_sensor1 = (message)
          console.log(`Received message ${message} from topic ${topic}`)
        }
        if(topic == 'home/sensor2'){
          this.dados_sensor2 = (message)
          console.log(`Received message ${message} from topic ${topic}`)
        }

      })
    },
    // 订阅主题
    doSubscribe(topic, qos) {
      //const { topic, qos } = topic, qos
      this.client.subscribe(topic, { qos }, (error, res) => {
        if (error) {
          console.log('Subscribe to topics error', error)
          return
        }
        this.subscribeSuccess = true
        console.log('Subscribe to topics res', res)
      })
    },
    // 取消订阅
    doUnSubscribe() {
      const { topic } = this.subscription
      this.client.unsubscribe(topic, error => {
        if (error) {
          console.log('Unsubscribe error', error)
        }
      })
    },
    // 发送消息
    doPublish() {
      const { topic, qos, payload } = this.publish
      this.client.publish(topic, payload, qos, error => {
        if (error) {
          console.log('Publish error', error)
        }
      })
    },


    // 断开连接
    destroyConnection() {
      if (this.client.connected) {
        try {
          this.client.end()
          this.client = {
            connected: false,
          }
          console.log('Successfully disconnected!')
        } catch (error) {
          console.log('Disconnect failed', error.toString())
        }
      }
    },

    async fetchData(){
      
     let response = await fetch('http://192.168.1.2:5000/sensor_banco/sensor1');
     let data = await response.json()

     this.dado = Array.from(data,x => parseInt(x[0]))
    },
    async fetchDataSensor2(){
      
     let response = await fetch('http://192.168.1.2:5000/sensor_banco/sensor2');
     let data = await response.json()

     this.fetch_sensor2 = Array.from(data,x => parseInt(x[0]))
    },

  },
  created: function(){
    let cont = 0
    if(cont === 0){
    this.createConnection(),
    this.doSubscribe('home/sensor1',0)
    this.doSubscribe('home/sensor2',1)
    cont = 1
    this.fetchData();
    this.fetchDataSensor2();
    }
    
    setInterval(() => this.fetchDataSensor2(), 60000);
    setInterval(() => this.fetchData(), 60000);
  }
}



</script>
