from setuptools import setup

package_name = 'kapal'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/robot_launch.py']),  # <-- tambah ini
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mas',
    maintainer_email='mas@robot.com',
    description='Package for controlling kapal',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'yolo_detector = kapal.yolo_detector:main',
            'decision_maker = kapal.decision_maker:main',
            'motor_controller = kapal.motor_controller:main',
        ],
    },
)
