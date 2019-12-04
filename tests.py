# tests.py

from unittest import TestCase, main as unittest_main
from app import app

class PlaylistsTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True


#     # tests.py
# class PlaylistsTests(TestCase):
#     ...
#     def test_index(self):
#         """Test the playlists homepage."""
#         result = self.client.get('/')
#         self.assertEqual(result.status, '200 OK')

class PlaylistsTests(TestCase):

    def test_new(self):
        """Test the new playlist creation page."""
        result = self.client.get('/playlists/new')
        self.assertEqual(result.status, '200 OK')

    @mock.patch('pymongo.collection.Collection.delete_one')
    def test_delete_playlist(self, mock_delete):
        form_data = {'_method': 'DELETE'}
        result = self.client.post(f'/playlists/{sample_playlist_id}/delete', data=form_data)
        self.assertEqual(result.status, '302 FOUND')
        mock_delete.assert_called_with({'_id': sample_playlist_id})



if __name__ == '__main__':
    unittest_main()