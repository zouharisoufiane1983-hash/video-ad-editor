from pathlib import Path

def export_video(clip, output, fps=24, codec="libx264", audio=True):
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    clip.write_videofile(
        str(output),
        fps=fps,
        codec=codec,
        audio=audio,
        ffmpeg_params=["-s", f"{clip.w}x{clip.h}"]
    )
