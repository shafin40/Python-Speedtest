import speedtest

def test_speed():
    # create a speedtest object
    st = speedtest.Speedtest()

    # perform a download speed test
    download_speed = st.download()

    # perform an upload speed test
    upload_speed = st.upload()

    # print the results
    print(f"Download speed: {download_speed / 1000000:.2f} Mbps")
    print(f"Upload speed: {upload_speed / 1000000:.2f} Mbps")

if __name__ == "__main__":
    test_speed()
