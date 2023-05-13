import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist,Point
from std_msgs.msg import String
from nav_msgs.msg import Odometry
#euler_from_quaternion, quaternion_from_euler
from tf_transformations import euler_from_quaternion
from math import atan2


first_time = True


class robot_controller(Node):

    def __init__(self):
        super().__init__('subscriebr_node')
        ## robot position
        self.x,self.y = 0.0,0.0
        # robot orientation
        self.theta = 0.0
        # target point index
        self.point = 0
        # target point list
        self.point_list = [(1.0,2.0,3.0),(4.0,5.0,6.0),(-7.0,8.0,9.0),(-6.0,-2.0,25.0),(1.0,2.0,3.0)]
        # publisher, controls robot velocity
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        # timer, calls publisher_callback every 0.02 seconds
        self.timer = self.create_timer(0.02, self.publisher_callback)
        # subscriber, gets robot position
        self.subscription = self.create_subscription(Odometry, '/odom', self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
            # get robot position
            self.x = msg.pose.pose.position.x
            self.y = msg.pose.pose.position.y
            # get robot orientation
            rot = msg.pose.pose.orientation
            #transfrom quaternion to an angle in radians
            (roll,pitch,self.theta) = euler_from_quaternion([rot.x,rot.y,rot.z,rot.w])
            
    def publisher_callback(self):
        goal = Point()
        speed = Twist()
        # get target point
        goal.x = self.point_list[self.point][0]
        goal.y = self.point_list[self.point][1]

        # calculate angle to target point
        inc_x = goal.x - self.x
        inc_y = goal.y - self.y
        angle_to_goal = atan2(inc_y,inc_x)

        # if robot is close to target point, go to next point
        if abs(self.x -self.point_list[self.point][0])<0.1 and abs(self.y -self.point_list[self.point][1])<0.1 :
            self.point += 1
            if self.point == len(self.point_list):
                self.point = 0

        # if robot is not facing target point, rotate
        if abs(angle_to_goal - self.theta) > 0.1:
            speed.linear.x = 0.0
            val = 0.3 if (angle_to_goal - self.theta) > 0 else -0.3
            speed.angular.z = val
            self.publisher.publish(speed)
        # if robot is facing target point, move forward
        else:
            speed.linear.x = 0.5
            speed.angular.z = 0.0
            self.publisher.publish(speed)
          


def main(args=None):
    rclpy.init(args=args)
    subscriebr_node = robot_controller()
    rclpy.spin(subscriebr_node)
    subscriebr_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()