from distutils.core import setup

setup(
  name = 'PyEyeTrack',         
  packages = find_packages(include = ['pyEyeTrack','pyEyeTrack.*']),   
  version = '0.3.6.5',      
  license='MIT',        
  description = """PyEyeTrack is a python-based pupil-tracking library. The library tracks eyes with the commodity webcam 
                and gives a real-time stream of eye coordinates. It provides the functionality of eye-tracking and 
                blink detection and encapsulates these in a generic interface that allows clients to use these 
                functionalities in a variety of use-cases.""", 
  authors = 'Kanchan Sarolkar, Kimaya Badhe, Neha Chaudhari, Samruddhi Kanhed and Shrirang Karandikar',                   
  author_email = 'pytracklibrary@gmail.com',      
  url = 'https://github.com/algoasylum/PyEyeTrack',  
  download_url = 'https://github.com/algoasylum/pyEyeTrack/archive/v_03_6_5.tar.gz',    
  keywords = ['Eye Tracking','blink detection','User Interface','Webcamera'], 
  install_requires=[
  'keyboard==0.13.3',
  'numpy==1.18.1',
  'opencv-python>=4.0.*',
  'pandas==0.24.0',
  'pyaudio==0.2.11',
  ],  
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
  ],
)