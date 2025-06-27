import speedtest

def test_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download = st.download() / 1_000_000  # Mbps
        upload = st.upload() / 1_000_000      # Mbps
        ping = st.results.ping
        return round(download, 2), round(upload, 2), round(ping, 2)
    except Exception:
        raise

