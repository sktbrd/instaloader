import instaloader
import requests
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import os
import random
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_caching import Cache

proxies = ["https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199693-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199694-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199695-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199696-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199697-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199698-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199699-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199700-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199701-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199702-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199703-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199704-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199705-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199706-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199707-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199708-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199709-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199710-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199711-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199712-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199713-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199714-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199715-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199716-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199717-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199718-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199719-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199720-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199721-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199722-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199723-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199724-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199725-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199726-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199727-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199728-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199729-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199730-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199731-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199732-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199733-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199734-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199735-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199736-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199737-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199738-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199739-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199740-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199741-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199742-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777",
           "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199743-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199744-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199745-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199746-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199747-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199748-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199749-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199750-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199751-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199752-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199753-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199754-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199755-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199756-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199757-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199758-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199759-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199760-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199761-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199762-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199763-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199764-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199765-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199766-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199767-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199768-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199769-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199770-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199771-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199772-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199773-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199774-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199775-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199776-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199777-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199778-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199779-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199780-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199781-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199782-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199783-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199784-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199785-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199786-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199787-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199788-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199789-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199790-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199791-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777", "https://customer-dudemyman-cc-us-st-us_georgia-sessid-0079199792-sesstime-1:Hashtagdub111!@pr.oxylabs.io:7777"]


def get_random_proxy():
    return random.choice(proxies)


os.environ["HTTPS_PROXY"] = get_random_proxy()
os.environ["no_proxy"] = "api.pinata.cloud"

config = {
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 3600
}
app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)

cache = Cache(app)

load_dotenv()  # Load environment variables from .env file


def download_post(post_id):
    print(f"Downloading post {post_id}")

    L = instaloader.Instaloader(
        download_pictures=True,
        download_videos=True,
        download_video_thumbnails=True,
        compress_json=False,
        download_geotags=False,
        post_metadata_txt_pattern=None,
        max_connection_attempts=3,
        download_comments=False,
        dirname_pattern="/tmp/{shortcode}",
        filename_pattern="{shortcode}",
    )

    post = instaloader.Post.from_shortcode(L.context, post_id)
    print(f"Got post meta {post_id}")

    L.download_post(post, target=f"/tmp/{post_id}")
    print(f"Downloaded media {post_id}")

    return post


def upload_post(post_id, post):
    # log post
    print(f"Uploading post {post}")

    sidecar_postfix = ""

    if post.typename == 'GraphSidecar':
        sidecar_postfix = "_1"

    if post.is_video:
        file_extension = '.mp4'
        thumbnail_extension = '.jpg'
    else:
        file_extension = '.jpg'
        thumbnail_extension = None

    file_path = f"/tmp/{post_id}/{post_id}{sidecar_postfix}{file_extension}"
    file_name = f"{post_id}{file_extension}"
    pinata_response = upload_to_pinata(file_path, file_name)

    if thumbnail_extension:
        thumbnail_path = f"/tmp/{post_id}/{post_id}{sidecar_postfix}{thumbnail_extension}"
        thumbnail_name = f"{post_id}{thumbnail_extension}"
        thumbnail_pinata_response = upload_to_pinata(
            thumbnail_path, thumbnail_name)
        return pinata_response, thumbnail_pinata_response

    return [pinata_response]


def upload_to_pinata(file_path, file_name):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    payload = {
        'pinataOptions': '{"cidVersion": 1}',
        'pinataMetadata': '{"name": "{file_name}", "keyvalues": {"company": "Collective"}}'
    }
    files = [
        ('file', (file_name, open(file_path, 'rb'), 'application/octet-stream'))
    ]
    headers = {
        'Authorization': f'Bearer {os.environ["PINATA_API_JWT"]}'
    }
    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)
    return response.json()


def custom_cache_key():
    return request.url + request.args.get('postId', None)


@app.route('/api', methods=['GET'])
@cache.cached(timeout=43200, key_prefix=custom_cache_key)
def api():
    post_id = request.args.get('postId', None)
    print(f"postId {post_id} {request} {request.args}")

    if post_id:
        print(f"Got postId as param {post_id}")
        try:
            post = download_post(post_id)
            pinata_response = upload_post(post_id, post)

            response = {
                'success': True,
                'post_id': post_id,
                'media_type': 'video' if post.is_video else 'image',
                'caption': post.caption,
                'url': f'https://www.instagram.com/p/{post_id}',
                'pinata_response': pinata_response
            }

        except Exception as e:
            response = {
                'success': False,
                'error': str(e)
            }

    else:
        print(f"Did not get postId {post_id}")
        response = {
            'success': False,
            'error': 'Please provide a postId as a search parameter.'
        }

    return jsonify(response)
