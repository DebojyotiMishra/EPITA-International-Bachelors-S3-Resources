package com.pham_mishra.parisairline.service;

import com.pham_mishra.parisairline.model.Book;
import com.pham_mishra.parisairline.repository.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class BookService {

    private final BookRepository bookRepository;

    @Autowired
    public BookService(BookRepository bookRepository) {
        this.bookRepository = bookRepository;
    }

    public List<Book> getAllBookings() {
        return bookRepository.findAll();
    }

    public Optional<Book> getBookingById(Long id) {
        return bookRepository.findById(id);
    }

    public Book saveBooking(Book booking) {
        return bookRepository.save(booking);
    }

    public Optional<Book> updateBooking(Long id, Book updatedBooking) {
        if (bookRepository.existsById(id)) {
            updatedBooking.setId(id);
            return Optional.of(bookRepository.save(updatedBooking));
        }
        return Optional.empty();
    }

    public void deleteBooking(Long id) {
        bookRepository.deleteById(id);
    }
}
