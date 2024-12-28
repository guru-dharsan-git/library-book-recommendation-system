import os
import requests
from PIL import Image
from io import BytesIO

# Create static/images directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

# Book cover URLs
book_covers = {
    'gatsby.jpg': 'https://m.media-amazon.com/images/I/71FTb9X6wsL._AC_UF1000,1000_QL80_.jpg',
    '1984.jpg': 'https://m.media-amazon.com/images/I/71kxa1-0mfL._AC_UF1000,1000_QL80_.jpg',
    'mockingbird.jpg': 'https://m.media-amazon.com/images/I/71FxgtFKcQL._AC_UF1000,1000_QL80_.jpg',
    'pride.jpg': 'https://m.media-amazon.com/images/I/71Q1tPupKjL._AC_UF1000,1000_QL80_.jpg',
    'catcher.jpg': 'https://m.media-amazon.com/images/I/61fgOuZfBGL._AC_UF1000,1000_QL80_.jpg',
    'hobbit.jpg': 'https://m.media-amazon.com/images/I/710+HcoP38L._AC_UF1000,1000_QL80_.jpg',
    'harry.jpg': 'https://m.media-amazon.com/images/I/81m1s4wIPML._AC_UF1000,1000_QL80_.jpg',
    'lotr.jpg': 'https://m.media-amazon.com/images/I/71jLBXtWJWL._AC_UF1000,1000_QL80_.jpg',
    'davinci.jpg': 'https://m.media-amazon.com/images/I/71s0NYR0+dL._AC_UF1000,1000_QL80_.jpg',
    'alchemist.jpg': 'https://m.media-amazon.com/images/I/71aFt4+OTOL._AC_UF1000,1000_QL80_.jpg',
    'hunger.jpg': 'https://m.media-amazon.com/images/I/71WSzS6zvCL._AC_UF1000,1000_QL80_.jpg',
    'dragon.jpg': 'https://m.media-amazon.com/images/I/71xX8L8dZhL._AC_UF1000,1000_QL80_.jpg',
    'narnia.jpg': 'https://m.media-amazon.com/images/I/81RuAzKrHkL._AC_UF1000,1000_QL80_.jpg',
    'brave.jpg': 'https://m.media-amazon.com/images/I/61+TlJCrbhL._AC_UF1000,1000_QL80_.jpg',
    'shining.jpg': 'https://m.media-amazon.com/images/I/71tFhdcC0XL._AC_UF1000,1000_QL80_.jpg',
    'road.jpg': 'https://m.media-amazon.com/images/I/71IJ1HC2a3L._AC_UF1000,1000_QL80_.jpg',
    'gone.jpg': 'https://m.media-amazon.com/images/I/71+1I4YTS9L._AC_UF1000,1000_QL80_.jpg',
    'kite.jpg': 'https://m.media-amazon.com/images/I/71QKQ9mwV7L._AC_UF1000,1000_QL80_.jpg',
    'help.jpg': 'https://m.media-amazon.com/images/I/61+vBsnR7xL._AC_UF1000,1000_QL80_.jpg',
    'pi.jpg': 'https://m.media-amazon.com/images/I/71KqO5tKUYL._AC_UF1000,1000_QL80_.jpg'
}

# Create a default book cover
def create_default_cover():
    img = Image.new('RGB', (800, 1200), color='#f0f0f0')
    img.save('static/images/default-book.jpg')

# Download and save book covers
def download_book_covers():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    for filename, url in book_covers.items():
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                img.save(f'static/images/{filename}')
                print(f'Successfully downloaded {filename}')
            else:
                print(f'Failed to download {filename}')
        except Exception as e:
            print(f'Error downloading {filename}: {str(e)}')

if __name__ == '__main__':
    create_default_cover()
    download_book_covers()
    print('Image download process completed!')
