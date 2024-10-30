import os
import instaloader

def download_video_from_inst_by_url(your_url : str) -> None:
    """Insert an your video url. Video must be saved to the folder where python file lies."""
    loader = instaloader.Instaloader(download_videos=True, download_comments=False, download_video_thumbnails=False, download_geotags=False, download_pictures=False)
    post_url = your_url
    shortcode = post_url.split("/")[-2]
    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
    
        loader.download_post(post, target="temp_folder")

        for filename in os.listdir("temp_folder"):
            if filename.endswith(".mp4"):
                os.rename(os.path.join("temp_folder", filename), "your_vid.mp4")
                print("Video downloaded successfully as 'your_vid.mp4'")
                break
        else:
            print("No video found in the post.")
    
        os.rmdir("temp_folder")

    except Exception as e:
        print("An error occurred:", e)