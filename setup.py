from distutils.core import setup
  

setup(name='pybullet_arm_course',
      version='1.0.0',
      install_requires=[
            'pybullet',
      ],
      description='PyBullet planning course',
      author='Alex LaGrassa, Tiffany Yu',
      author_email='lagrassa@cmu.edu, tiffany2@cmu.edu',
      packages=['pybullet_arm_course', 'pybullet_arm_course.pybullet_tools', 'pybullet_arm_course.pybullet_tools.ikfast'],
      package_data={"pybullet_arm_course": ['assets/*']}
     )

