from distutils.core import setup
  

setup(name='pybullet_arm_course',
      version='2.0.0',
      install_requires=[
            'pybullet',
      ],
      description='PyBullet planning course',
      author='Alex LaGrassa, Tiffany Yu, Jessie Grosen',
      author_email='lagrassa@cmu.edu, tiffany2@cmu.edu',
      packages=['pybullet_arm_course', 'pybullet_arm_course.pybullet_tools', 'pybullet_arm_course.pybullet_tools.ikfast'],
     )

