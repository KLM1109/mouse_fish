import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;

public class RandomMouseMoverGUI {

    // 定义常量
    private static boolean stopProgram = false;
    private static long lastEventTime = 0;
    private static final long RESUME_DELAY = 120000; // 2分钟
    private static final int MOVE_INTERVAL = 10000; // 每次移动间隔10秒
    private static Robot robot;
    private static Timer timer;

    public static void main(String[] args) {
        // 使用 SwingUtilities 确保界面在事件调度线程中创建
        SwingUtilities.invokeLater(() -> {
            try {
                // 初始化 Robot 对象
                robot = new Robot();

                // 创建 GUI 窗口
                JFrame frame = new JFrame("鼠标自动移动控制");
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.setSize(400, 200);
                frame.setLocationRelativeTo(null); // 居中显示

                // 创建启动/停止按钮
                JButton toggleButton = new JButton("启动鼠标移动");
                toggleButton.setFont(new Font("Arial", Font.PLAIN, 20));
                toggleButton.setPreferredSize(new Dimension(200, 50));

                // 按钮点击事件：启动或停止鼠标移动
                toggleButton.addActionListener(e -> {
                    if (stopProgram) {
                        // 启动鼠标移动
                        stopProgram = false;
                        toggleButton.setText("停止鼠标移动");
                        startRandomMouseMove();
                        frame.setVisible(false); // 隐藏窗口
                    } else {
                        // 停止鼠标移动
                        stopProgram = true;
                        toggleButton.setText("启动鼠标移动");
                        if (timer != null) {
                            timer.cancel();
                        }
                        frame.setVisible(true); // 显示窗口
                    }
                });

                // 布局设置
                JPanel panel = new JPanel();
                panel.setLayout(new BorderLayout());
                panel.add(toggleButton, BorderLayout.CENTER);
                frame.add(panel);

                // 显示 GUI 窗口
                frame.setVisible(true);

                // 添加鼠标事件监听
                MouseListener mouseListener = new MouseListener(frame);
                MouseMotionListener mouseMotionListener = new MouseMotionListener();

                Toolkit.getDefaultToolkit().addAWTEventListener(mouseListener, AWTEvent.MOUSE_EVENT_MASK);
                Toolkit.getDefaultToolkit().addAWTEventListener(mouseMotionListener, AWTEvent.MOUSE_MOTION_EVENT_MASK);

            } catch (AWTException e) {
                e.printStackTrace();
            }
        });
    }

    // 随机移动鼠标
    private static void startRandomMouseMove() {
        timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                // 如果程序需要停止，则退出
                if (stopProgram) {
                    timer.cancel();
                    System.out.println("程序已停止.");
                    return;
                }

                // 检查上次事件是否超过 2 分钟
                long currentTime = System.currentTimeMillis();
                if (currentTime - lastEventTime >= RESUME_DELAY) {
                    // 生成随机的屏幕位置
                    Random rand = new Random();
                    int screenWidth = Toolkit.getDefaultToolkit().getScreenSize().width;
                    int screenHeight = Toolkit.getDefaultToolkit().getScreenSize().height;

                    int randomX = rand.nextInt(screenWidth);
                    int randomY = rand.nextInt(screenHeight);

                    // 移动鼠标
                    robot.mouseMove(randomX, randomY);
                    System.out.println("鼠标随机移动到: (" + randomX + ", " + randomY + ")");
                    lastEventTime = currentTime; // 更新最后事件时间
                }
            }
        }, 0, MOVE_INTERVAL); // 每隔 10 秒执行一次
    }

    // 鼠标点击事件监听
    private static class MouseListener implements AWTEventListener {
        private JFrame frame;

        public MouseListener(JFrame frame) {
            this.frame = frame;
        }

        @Override
        public void eventDispatched(AWTEvent event) {
            if (event instanceof MouseEvent) {
                MouseEvent me = (MouseEvent) event;
                if (me.getID() == MouseEvent.MOUSE_PRESSED) {
                    if (me.getButton() == MouseEvent.BUTTON1) { // 检查是否是鼠标左键
                        System.out.println("检测到左键点击，程序退出...");
                        stopProgram = true;
                        if (timer != null) {
                            timer.cancel(); // 停止定时器
                        }
                        frame.setVisible(true); // 显示窗口
                    }
                }
                lastEventTime = System.currentTimeMillis(); // 更新最近的事件时间
            }
        }
    }

    // 鼠标移动事件监听
    private static class MouseMotionListener implements AWTEventListener {
        @Override
        public void eventDispatched(AWTEvent event) {
            if (event instanceof MouseEvent) {
                MouseEvent me = (MouseEvent) event;
                lastEventTime = System.currentTimeMillis(); // 更新最近的事件时间
            }
        }
    }
}
