import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist,Point
from std_msgs.msg import String
from nav_msgs.msg import Odometry
#euler_from_quaternion, quaternion_from_euler
from tf_transformations import euler_from_quaternion
from math import atan2


first_time = True




class Subscrieber_Node(Node):
    def __init__(self):
        super().__init__('subscriebr_node')
        self.subscription = self.create_subscription(String, 'chatter', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

        

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

    
class Subscrieber_Node2(Node):
    def __init__(self):
        super().__init__('subscriebr_node')
        self.x,self.y,self.z = 0,0,0
        self.point = 0
        self.subscription = self.create_subscription(Odometry, '/odom', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.point_list = [(1,2,3),(4,5,6),(7,8,9),(1,2,25),(1,2,3),(4,5,6),(7,8,9),(100,2,25)]
        self.timer = self.create_timer(0.5, self.publisher_callback)

    def point_distance(self,point1):
        return ((point1[0] - self.x)**2 + (point1[1] - self.y)**2)**0.5
    def direction(self,point):
        x_dir = (point[0] - self.x)
        y_dir = (point[1] - self.y)
        
        # self.get_logger().info('I heard: x"%s"' % x_dir)
        # self.get_logger().info('I heard: x"%s"' % y_dir)
        # self.get_logger().info('I heard: x"%s"' % str(abs(self.x -self.point_list[self.point][0])))
        # self.get_logger().info('I heard: y"%s"' % str(abs(self.y -self.point_list[self.point][1])))
        # self.get_logger().info('I heard: z"%s"' % str(point))

        return x_dir,y_dir


    def listener_callback(self, msg):
        if first_time:
            self.x = msg.pose.pose.position.x
            self.y = msg.pose.pose.position.y
          

        if abs(self.x -self.point_list[self.point][0])<1  :
            self.point += 1
            if self.point == len(self.point_list):
                self.point = 0
        
        self.get_logger().info('I heard: x"%s"' % msg.pose.pose.position.x)
       

    def publisher_callback(self):
        msg = Twist()
        msg.linear.x , msg.linear.y  = self.direction(self.point_list[self.point])
        self.publisher.publish(msg)
        self.x = self.x + float(msg.linear.x)
        self.y = self.y + float(msg.linear.y)

class Subscrieber_Node3(Node):

    def __init__(self):
        super().__init__('subscriebr_node')
        self.x,self.y = 0.0,0.0
        self.theta = 0.0
        self.point = 0
        self.point_list = [(1.0,2.0,3.0),(4.0,5.0,6.0),(-7.0,8.0,9.0),(-6.0,-2.0,25.0),(1.0,2.0,3.0)]
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.02, self.publisher_callback)
        self.subscription = self.create_subscription(Odometry, '/odom', self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
        
            self.x = msg.pose.pose.position.x
            self.y = msg.pose.pose.position.y
            rot = msg.pose.pose.orientation
            (roll,pitch,self.theta) = euler_from_quaternion([rot.x,rot.y,rot.z,rot.w])
            
    def publisher_callback(self):
        goal = Point()
        speed = Twist()
        goal.x = self.point_list[self.point][0]
        goal.y = self.point_list[self.point][1]

        inc_x = goal.x - self.x
        inc_y = goal.y - self.y

        angle_to_goal = atan2(inc_y,inc_x)

        if abs(self.x -self.point_list[self.point][0])<0.1 and abs(self.y -self.point_list[self.point][1])<0.1 :
            self.point += 1
            if self.point == len(self.point_list):
                self.point = 0

        if abs(angle_to_goal - self.theta) > 0.1:
            speed.linear.x = 0.0
            val = 0.3 if (angle_to_goal - self.theta) > 0 else -0.3
            speed.angular.z = val
            self.publisher.publish(speed)
        else:
            speed.linear.x = 0.5
            speed.angular.z = 0.0
            self.publisher.publish(speed)
          


def main(args=None):
    rclpy.init(args=args)
    subscriebr_node = Subscrieber_Node3()
    rclpy.spin(subscriebr_node)
    subscriebr_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()