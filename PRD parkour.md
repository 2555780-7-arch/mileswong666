[Subway Dash 2D] PRD
一、專案概述
專案名稱： Subway Dash 2D

一句話描述： 一款基於 Web 的單文件輕量級 2D 無限跑酷遊戲，採用塗鴉風格，玩家需在加速的地鐵軌道上通過跳躍與翻滾躲避障礙並收集金幣。

版本： v1.0 (MVP)

二、問題與目標
問題陳述
用戶在短暫休息或通勤時，需要一款無需下載安裝、載入即玩、節奏明快的休閒遊戲來打發時間。

現有的 Web 遊戲往往依賴大量外部資源加載，導致啟動緩慢或受網絡環境限制。

目標
核心目標： 提供一個零外部依賴（Single-file HTML）、響應迅速且具備完整核心循環（Core Loop）的跑酷體驗。

體驗目標： 透過視覺差背景、合成音效與粒子文字反饋，在有限的技術架構下提供具備「打擊感」的遊戲體驗。

三、目標用戶
用戶特徵
休閒玩家： 喜歡操作簡單但考驗反應速度的遊戲。

上班族/學生： 利用碎片化時間（5-10分鐘）進行娛樂。

Web 開發愛好者： 對 Canvas 遊戲開發與代碼實現感興趣的用戶。

用戶需求
低門檻： 打開瀏覽器即可玩，支援鍵盤與觸控。

即時反饋： 操作無延遲，失敗後可立即重開（Instant Replay）。

成就感： 透過積分積累與難度遞增獲得挑戰樂趣。

四、用戶故事
用戶故事1（操作）： 作為玩家，我想要透過鍵盤或觸控屏幕控制角色跳躍和翻滾，以便躲避高低不同的障礙物。

用戶故事2（得分）： 作為玩家，我想要在奔跑過程中收集金幣，以便獲得分數並看到浮動的加分特效。

用戶故事3（反饋）： 作為玩家，我想要在跳躍、撞擊或吃金幣時聽到音效，以便獲得更好的沈浸感。

用戶故事4（重開）： 作為玩家，當我撞到障礙物失敗時，我想要看到結算畫面並能一鍵重新開始。

五、功能需求與驗收標準
功能1：角色控制系統 (Player Controller)
描述： 控制角色在跑道上的垂直運動，包含跳躍與翻滾。

驗收標準（Given/When/Then）：

Given 遊戲正在進行中。

When 玩家按下 ↑、Space、W 或向上滑動（Touch）。

Then 角色應執行跳躍動作（Y軸向上位移），且播放 Jump 音效。

When 玩家按下 ↓、S 或向下滑動（Touch）。

Then 角色應執行翻滾動作（高度降低至原來的 50%），持續 40 幀後自動恢復站立。

When 角色處於空中（跳躍狀態）。

Then 再次按下翻滾鍵應使角色快速下墜（重力加速）。

功能2：障礙物生成與碰撞 (Obstacle System)
描述： 隨機生成需要不同操作應對的障礙物，並處理碰撞邏輯。

驗收標準：

Given 遊戲隨時間推移。

When 生成障礙物時。

Then 應有 30% 機率生成「懸空路牌」（需翻滾躲避），70% 機率生成「地面路障」（需跳躍躲避）。

When 角色 Hitbox 與障礙物重疊。

Then 觸發 gameOver()，停止遊戲循環，播放 Hit 音效，並顯示 "BUSTED" UI。

功能3：金幣與計分系統 (Scoring System)
描述： 金幣生成、收集判定及 UI 分數更新。

驗收標準：

Given 遊戲進行中。

When 角色進入金幣 40px 半徑範圍內。

Then 金幣消失，分數+1，播放清脆 Coin 音效，並在角色位置生成浮動的 "+1" 噴漆文字特效。

When 遊戲畫面更新。

Then 右上角 HUD 應即時顯示當前金幣數量。

功能4：遊戲進程與環境 (Game Loop & Environment)
描述： 隨著時間增加難度，以及繪製視覺差背景。

驗收標準：

Given 遊戲正在運行。

When 每經過一幀。

Then gameSpeed 應增加 0.002，使遊戲節奏逐漸變快。

When 繪製背景。

Then 遠景城市與近景鐵軌應以不同速度移動，產生視差滾動效果（Parallax Scrolling）。

功能5：音頻合成系統 (Web Audio API)
描述： 不使用外部 MP3 文件，使用瀏覽器原生 API 合成音效。

驗收標準：

Given 玩家執行動作。

Then 跳躍應產生頻率滑升的振盪音；吃金幣應產生高頻三角波音效；撞擊應產生鋸齒波噪音。

六、技術約束
必須遵守
單文件架構： HTML, CSS, JavaScript 必須整合在同一個文件中，禁止引用外部 .png 或 .mp3 文件。

圖形渲染： 必須使用 HTML5 Canvas 2D Context 繪製所有圖形（角色、背景、障礙物）。

字體依賴： 僅依賴 Google Fonts (Black Ops One, Fredoka One)，需確保網絡加載處理。

響應式設計： 遊戲容器需在瀏覽器視窗中置中，並適配桌面與移動端視圖。

兼容性要求
瀏覽器： Chrome, Firefox, Safari, Edge (最新版本)。

輸入設備： 鍵盤 (Keyboard Events) 與 觸控屏 (Touch Events)。

不要做
不要使用任何重型遊戲引擎（如 Unity, Phaser）。

不要將邏輯與視圖過度耦合，保持 update() 與 draw() 分離。

七、現有代碼
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subway Dash 2D</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Black+Ops+One&family=Fredoka+One&display=swap');

        body {
            margin: 0;
            overflow: hidden;
            background-color: #333;
            font-family: 'Fredoka One', cursive;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        #game-container {
            position: relative;
            width: 800px;
            height: 450px;
            background: #87CEEB;
            overflow: hidden;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
            border: 4px solid #fff;
            border-radius: 15px;
        }

        canvas { display: block; }

        /* UI 覆蓋層 */
        .ui-layer {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background: rgba(0, 0, 0, 0.6);
            z-index: 10;
            backdrop-filter: blur(4px);
            transition: opacity 0.3s;
        }

        .hidden { opacity: 0; pointer-events: none; }

        /* 標題風格 */
        h1 {
            font-family: 'Black Ops One', cursive;
            font-size: 60px;
            color: #ffcc00; /* 金黃色 */
            text-shadow: 
                3px 3px 0px #ff0055, 
                6px 6px 0px #000;
            transform: skew(-10deg) rotate(-5deg);
            margin: 0 0 20px 0;
            letter-spacing: 2px;
        }

        .score-hud {
            position: absolute;
            top: 15px;
            right: 20px;
            font-size: 32px;
            color: #fff;
            text-shadow: 2px 2px 0 #000;
            display: flex;
            align-items: center;
            gap: 10px;
            z-index: 5;
        }

        .coin-icon {
            width: 30px; height: 30px;
            background: gold;
            border-radius: 50%;
            border: 3px solid #d4af37;
            box-shadow: inset 2px 2px 5px rgba(255,255,255,0.5);
            display: inline-block;
        }

        button {
            background: #00d2ff;
            border: 4px solid #fff;
            color: #fff;
            padding: 15px 40px;
            font-size: 24px;
            font-family: 'Fredoka One', cursive;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 6px 0 #0099cc, 0 10px 10px rgba(0,0,0,0.3);
            transition: transform 0.1s;
            text-transform: uppercase;
        }

        button:hover { transform: scale(1.05); }
        button:active { transform: scale(0.95) translateY(4px); box-shadow: 0 2px 0 #0099cc; }

        .controls-hint {
            margin-top: 20px;
            color: #fff;
            font-size: 16px;
            text-shadow: 1px 1px 2px black;
            display: flex;
            gap: 20px;
        }
        .key {
            background: rgba(255,255,255,0.2);
            padding: 5px 10px;
            border-radius: 5px;
            border: 2px solid #fff;
        }

        /* 噴漆效果 */
        .spray-text {
            position: absolute;
            font-size: 24px;
            color: #ff0055;
            font-weight: bold;
            pointer-events: none;
            animation: floatUp 1s forwards;
            text-shadow: 2px 2px 0 #fff;
        }

        @keyframes floatUp {
            0% { transform: translateY(0) scale(1); opacity: 1; }
            100% { transform: translateY(-50px) scale(1.5); opacity: 0; }
        }
    </style>
</head>
<body>

    <div id="game-container">
        <canvas id="gameCanvas" width="800" height="450"></canvas>
        
        <div class="score-hud">
            <div class="coin-icon"></div>
            <span id="coinScore">0</span>
        </div>

        <div id="ui-layer" class="ui-layer">
            <h1>SUBWAY DASH</h1>
            <button onclick="startGame()">TAP TO PLAY</button>
            <div class="controls-hint">
                <span><span class="key">↑</span> JUMP</span>
                <span><span class="key">↓</span> ROLL</span>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const uiLayer = document.getElementById('ui-layer');
        const coinScoreEl = document.getElementById('coinScore');
        const container = document.getElementById('game-container');

        // 音效合成
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        function playSound(type) {
            if (audioCtx.state === 'suspended') audioCtx.resume();
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.connect(gain);
            gain.connect(audioCtx.destination);

            if (type === 'jump') {
                osc.frequency.setValueAtTime(300, audioCtx.currentTime);
                osc.frequency.linearRampToValueAtTime(600, audioCtx.currentTime + 0.1);
                gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
                gain.gain.linearRampToValueAtTime(0, audioCtx.currentTime + 0.1);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.1);
            } else if (type === 'coin') {
                osc.type = 'triangle'; // 清脆的聲音
                osc.frequency.setValueAtTime(1200, audioCtx.currentTime);
                osc.frequency.linearRampToValueAtTime(1800, audioCtx.currentTime + 0.1);
                gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
                gain.gain.linearRampToValueAtTime(0, audioCtx.currentTime + 0.1);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.1);
            } else if (type === 'hit') {
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(100, audioCtx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(10, audioCtx.currentTime + 0.3);
                gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
                gain.gain.linearRampToValueAtTime(0, audioCtx.currentTime + 0.3);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.3);
            }
        }

        // 遊戲參數
        let gameSpeed = 8;
        let score = 0;
        let coins = 0;
        let isRunning = false;
        let frame = 0;

        // 地面高度
        const groundHeight = 60;
        const groundY = canvas.height - groundHeight;

        // 玩家物件
        const player = {
            x: 100,
            y: groundY,
            w: 40,
            h: 70, // 站立高度
            h_stand: 70,
            h_roll: 35, // 翻滾高度
            dy: 0,
            jumpForce: -16,
            gravity: 0.8,
            grounded: true,
            rolling: false,
            rollTimer: 0,
            colorHead: '#ffcc00', // 塗鴉金
            colorBody: '#ff0055', // 塗鴉紅
            colorLegs: '#333'
        };

        // 物件池
        let obstacles = [];
        let coinsList = [];
        let particles = [];
        let bgOffset = 0;

        function startGame() {
            isRunning = true;
            uiLayer.classList.add('hidden');
            obstacles = [];
            coinsList = [];
            particles = [];
            coins = 0;
            score = 0;
            gameSpeed = 8;
            coinScoreEl.innerText = "0";
            
            player.y = groundY - player.h;
            player.dy = 0;
            
            loop();
        }

        function loop() {
            if (!isRunning) return;
            
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            update();
            draw();
            
            requestAnimationFrame(loop);
        }

        function update() {
            frame++;
            gameSpeed += 0.002; // 緩慢加速

            // --- 背景視差 ---
            bgOffset -= gameSpeed * 0.5;
            if (bgOffset <= -canvas.width) bgOffset = 0;

            // --- 玩家物理 ---
            // 跳躍與重力
            if (!player.grounded) {
                player.dy += player.gravity;
                player.y += player.dy;
            }

            // 地面碰撞
            if (player.y + player.h >= groundY) {
                player.y = groundY - player.h;
                player.dy = 0;
                player.grounded = true;
            } else {
                player.grounded = false;
            }

            // 翻滾邏輯
            if (player.rolling) {
                player.h = player.h_roll;
                player.rollTimer--;
                if (player.rollTimer <= 0) {
                    player.rolling = false;
                    player.y -= (player.h_stand - player.h_roll); // 恢復站立位置修正
                    player.h = player.h_stand;
                }
            }

            // --- 生成障礙物 ---
            if (frame % Math.floor(1000 / gameSpeed) === 0) {
                let type = Math.random();
                // 30% 生成高障礙 (需翻滾)，70% 生成低障礙 (需跳躍)
                if (type < 0.3) {
                    // 高障礙 (Sign)
                    obstacles.push({
                        x: canvas.width,
                        y: groundY - 110, // 懸空
                        w: 70,
                        h: 60,
                        type: 'sign'
                    });
                } else {
                    // 低障礙 (Barrier)
                    obstacles.push({
                        x: canvas.width,
                        y: groundY - 50,
                        w: 50,
                        h: 50,
                        type: 'barrier'
                    });
                }
                
                // 生成金幣 (跟隨障礙物或獨立生成)
                spawnCoins();
            }

            // --- 更新障礙物 ---
            for (let i = obstacles.length - 1; i >= 0; i--) {
                let obs = obstacles[i];
                obs.x -= gameSpeed;

                // 碰撞檢測
                if (
                    player.x < obs.x + obs.w - 10 &&
                    player.x + player.w > obs.x + 10 &&
                    player.y < obs.y + obs.h - 10 &&
                    player.y + player.h > obs.y + 10
                ) {
                    gameOver();
                }

                if (obs.x + obs.w < 0) obstacles.splice(i, 1);
            }

            // --- 更新金幣 ---
            for (let i = coinsList.length - 1; i >= 0; i--) {
                let c = coinsList[i];
                c.x -= gameSpeed;
                c.rot += 0.2; // 旋轉動畫

                // 吃金幣
                let centerX = player.x + player.w/2;
                let centerY = player.y + player.h/2;
                let dist = Math.sqrt((centerX - c.x)**2 + (centerY - c.y)**2);
                
                if (dist < 40) { // 吸附範圍
                    coinsList.splice(i, 1);
                    coins++;
                    coinScoreEl.innerText = coins;
                    playSound('coin');
                    createFloatingText("+1", player.x, player.y);
                } else if (c.x < -20) {
                    coinsList.splice(i, 1);
                }
            }
        }

        function spawnCoins() {
            // 在空中生成一排金幣
            if (Math.random() > 0.5) {
                let startX = canvas.width + 100;
                let heightLevel = Math.random() > 0.5 ? groundY - 150 : groundY - 40;
                for(let i=0; i<3; i++) {
                    coinsList.push({
                        x: startX + i * 50,
                        y: heightLevel,
                        rot: 0
                    });
                }
            }
        }

        function draw() {
            // 1. 畫背景 (城市剪影)
            // 遠景
            ctx.fillStyle = '#0066cc'; // 深藍天
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // 城市層
            ctx.fillStyle = '#004080';
            for(let i=0; i<10; i++) {
                let h = 100 + Math.sin(i*132)*50;
                ctx.fillRect((bgOffset/2 + i * 150) % (canvas.width+150) - 150, groundY - h, 100, h);
            }
            
            // 2. 畫鐵軌 (地面)
            ctx.fillStyle = '#555'; // 碎石路
            ctx.fillRect(0, groundY, canvas.width, groundHeight);
            
            // 枕木效果 (移動感)
            ctx.fillStyle = '#333';
            let tieSpacing = 40;
            let tieOffset = (bgOffset * 2) % tieSpacing;
            for (let x = tieOffset; x < canvas.width; x += tieSpacing) {
                ctx.fillRect(x, groundY + 5, 20, groundHeight - 10);
            }
            // 鐵軌線
            ctx.fillStyle = '#888';
            ctx.fillRect(0, groundY + 10, canvas.width, 5);
            ctx.fillRect(0, groundY + groundHeight - 15, canvas.width, 5);

            // 3. 畫障礙物
            obstacles.forEach(obs => {
                if (obs.type === 'barrier') {
                    // 紅白路障
                    ctx.fillStyle = '#ff3333';
                    ctx.fillRect(obs.x, obs.y, obs.w, obs.h);
                    ctx.fillStyle = '#fff';
                    ctx.fillRect(obs.x, obs.y + 10, obs.w, 10);
                    ctx.fillRect(obs.x, obs.y + 30, obs.w, 10);
                } else {
                    // 高處招牌
                    ctx.fillStyle = '#009944'; // 綠色路牌
                    ctx.fillRect(obs.x, obs.y, obs.w, obs.h);
                    ctx.fillStyle = '#fff';
                    ctx.font = 'bold 12px Arial';
                    ctx.fillText('SUBWAY', obs.x + 5, obs.y + 20);
                    ctx.fillText('->', obs.x + 20, obs.y + 40);
                    // 支柱
                    ctx.fillStyle = '#444';
                    ctx.fillRect(obs.x + 5, 0, 5, obs.y);
                    ctx.fillRect(obs.x + obs.w - 10, 0, 5, obs.y);
                }
            });

            // 4. 畫金幣
            coinsList.forEach(c => {
                ctx.save();
                ctx.translate(c.x, c.y);
                // 旋轉效果 (縮放寬度)
                let scaleX = Math.abs(Math.cos(c.rot));
                ctx.scale(scaleX, 1);
                
                ctx.beginPath();
                ctx.arc(0, 0, 15, 0, Math.PI * 2);
                ctx.fillStyle = 'gold';
                ctx.fill();
                ctx.lineWidth = 3;
                ctx.strokeStyle = '#d4af37';
                ctx.stroke();
                
                // 閃光
                ctx.fillStyle = '#fff';
                ctx.beginPath();
                ctx.arc(-5, -5, 3, 0, Math.PI*2);
                ctx.fill();
                
                ctx.restore();
            });

            // 5. 畫玩家 (簡單的塗鴉風格人物)
            ctx.save();
            ctx.translate(player.x, player.y);
            
            // 身體 (帽T)
            ctx.fillStyle = player.colorBody;
            ctx.fillRect(0, 0, player.w, player.h - 20);
            
            // 頭/帽子
            ctx.fillStyle = player.colorHead;
            ctx.fillRect(-5, -10, player.w + 10, 20); // 帽緣
            
            // 褲子
            ctx.fillStyle = player.colorLegs;
            ctx.fillRect(5, player.h - 25, 10, 25); // 左腿
            ctx.fillRect(25, player.h - 25, 10, 25); // 右腿

            // 背包 (噴漆罐)
            ctx.fillStyle = '#00d2ff';
            ctx.fillRect(-10, 10, 10, 20);

            ctx.restore();
        }

        function createFloatingText(text, x, y) {
            const el = document.createElement('div');
            el.className = 'spray-text';
            el.innerText = text;
            el.style.left = (container.offsetLeft + x) + 'px';
            el.style.top = (container.offsetTop + y) + 'px';
            document.body.appendChild(el);
            setTimeout(() => el.remove(), 1000);
        }

        function gameOver() {
            isRunning = false;
            playSound('hit');
            uiLayer.classList.remove('hidden');
            document.querySelector('h1').innerText = "BUSTED!";
            document.querySelector('button').innerText = "TRY AGAIN";
        }

        // --- 控制 ---
        function handleInput(action) {
            if (!isRunning) return;

            if (action === 'jump') {
                if (player.grounded) {
                    player.dy = player.jumpForce;
                    player.grounded = false;
                    player.rolling = false; // 取消翻滾
                    player.h = player.h_stand;
                    playSound('jump');
                }
            } else if (action === 'roll') {
                if (!player.rolling && player.grounded) {
                    player.rolling = true;
                    player.rollTimer = 40; // 翻滾持續時間
                    player.y += (player.h_stand - player.h_roll); // 瞬間壓低
                } else if (!player.grounded) {
                    // 空中快速下墜
                    player.dy = 15;
                }
            }
        }

        document.addEventListener('keydown', (e) => {
            if (e.code === 'ArrowUp' || e.code === 'Space' || e.code === 'KeyW') handleInput('jump');
            if (e.code === 'ArrowDown' || e.code === 'KeyS') handleInput('roll');
        });

        // 觸控支持
        let touchStartY = 0;
        document.addEventListener('touchstart', e => {
            touchStartY = e.touches[0].clientY;
        });
        document.addEventListener('touchend', e => {
            let touchEndY = e.changedTouches[0].clientY;
            let diff = touchStartY - touchEndY;
            if (Math.abs(diff) > 30) {
                if (diff > 0) handleInput('jump'); // 上滑
                else handleInput('roll'); // 下滑
            } else {
                handleInput('jump'); // 點擊
            }
        });

    </script>
</body>
</html>